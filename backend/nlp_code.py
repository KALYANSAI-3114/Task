import spacy
import re
from datetime import datetime, timedelta

nlp = spacy.load("en_core_web_sm")

def parse_query(text):
    text_l = text.lower()
    doc = nlp(text)

    # defaults
    intent = "list"
    metric = "Marked Up Cost"
    group_by = None
    filters = {}
    limit = None
    order_by = None
    date_filter = None

    # -------- INTENT DETECTION --------
    synonyms_count = ["how many", "count", "number of", "total shipments"]
    synonyms_sum = ["total", "sum", "overall", "total cost", "shipment cost", "charges"]
    synonyms_top = ["top", "highest", "most expensive", "costliest"]
    synonyms_last7 = ["last 7 days", "past week", "past 7 days"]
    synonyms_month = ["this month", "current month"]

    if any(word in text_l for word in synonyms_count):
        intent = "count"

    elif any(word in text_l for word in synonyms_sum):
        intent = "sum"
        metric = "Marked Up Cost"

    elif any(word in text_l for word in synonyms_top):
        intent = "list"
        numbers = re.findall(r"\d+", text_l)
        limit = int(numbers[0]) if numbers else 5
        order_by = "`Marked Up Cost` DESC"

    if "group" in text_l or "analysis" in text_l:
        if "status" in text_l: group_by = "Status"
        elif "carrier" in text_l: group_by = "Carrier"
        elif "shipment type" in text_l: group_by = "Shipment Type"

    if any(x in text_l for x in synonyms_last7):
        date_filter = ("Ship Date", datetime.now() - timedelta(days=7))

    if any(x in text_l for x in synonyms_month):
        date_filter = ("month", None)

    # entities fallback
    for ent in doc.ents:
        if ent.text.lower() in ["fedex","ups","dhl"]:
            filters["Carrier"] = ent.text

    if "pending" in text_l: filters["Delivery Status"] = "Pending"
    if "draft" in text_l: filters["Delivery Status"] = "Draft"

    return {
        "intent": intent,
        "metric": metric,
        "filters": filters,
        "group_by": group_by,
        "date_filter": date_filter,
        "limit": limit,
        "order_by": order_by
    }
