def build_sql(parsed):
    intent = parsed["intent"]
    metric = parsed["metric"]
    filters = parsed["filters"]
    group_by = parsed["group_by"]
    limit = parsed["limit"]
    order_by = parsed["order_by"]
    date_filter = parsed["date_filter"]

    # Default query (runs if NLP cannot detect intent) 👇
    sql = "SELECT * FROM final_shipping_data"

    if intent == "count":
        sql = "SELECT COUNT(*) AS result FROM final_shipping_data"

    elif intent == "sum":
        sql = f"SELECT SUM(`{metric}`) AS result FROM final_shipping_data"

    conditions = []

    # Filters
    for col, val in filters.items():
        conditions.append(f"`{col}` = '{val}'")

    # Dates
    if date_filter:
        if date_filter[0] == "month":
            conditions.append("MONTH(`Ship Date`) = MONTH(CURDATE()) AND YEAR(`Ship Date`) = YEAR(CURDATE())")
        else:
            conditions.append(f"`Ship Date` >= '{date_filter[1].strftime('%Y-%m-%d')}'")

    if conditions:
        sql += " WHERE " + " AND ".join(conditions)

    # GROUP BY logic
    if group_by:
        sql = f"SELECT `{group_by}`, COUNT(*) AS total_shipments, SUM(`{metric}`) AS total_cost FROM final_shipping_data"
        if conditions:
            sql += " WHERE " + " AND ".join(conditions)
        sql += f" GROUP BY `{group_by}`"
        return sql

    # Sorting & limit for top shipments
    if order_by:
        sql += f" ORDER BY {order_by}"

    if limit:
        sql += f" LIMIT {limit}"

    return sql    # final SQL returned always
