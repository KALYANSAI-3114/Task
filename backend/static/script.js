async function askQuery(){
    const question = document.getElementById("queryinput").value.trim();  
    const responseBox = document.getElementById("responseBox");

    if(!question){
        responseBox.innerHTML = `<p style="color:red;">Please enter a query.</p>`;
        return;
    }

    const res = await fetch("/query", {
        method:"POST",
        headers:{ "Content-Type":"application/json" },
        body:JSON.stringify({ question })
    });

    const data = await res.json();

    // Error handling
    if(data.error){
        responseBox.innerHTML = `<p style="color:red;">${data.error}</p>`;
        return;
    }

    const result = data.result;
    const intent = data.intent?.intent || "";        // read intent from parsed data
    const group_by = data.intent?.group_by || null;  // group detection

    let displayText = "";

    // ------------------- COUNT -------------------
    if(intent === "count" || question.toLowerCase().includes("how many")){
        displayText = `📦 Shipments count: <b>${result[0].result || 0}</b>`;
    }

    // ------------------- TOTAL / SUM -------------------
    else if(intent === "sum" || question.toLowerCase().includes("total") || question.toLowerCase().includes("sum")){
        displayText = `💰 Total shipment cost: <b>${result[0].result || 0}</b>`;
    }

    // ------------------- GROUP BY ANALYSIS -------------------
    else if(group_by){ 
        displayText = `<b>📊 Cost Analysis grouped by <u>${group_by}</u>:</b><br><pre>${JSON.stringify(result, null, 2)}</pre>`;
    }

    // ------------------- DEFAULT LIST OUTPUT -------------------
    else{
        displayText = `<b>Results:</b><br><pre>${JSON.stringify(result, null, 2)}</pre>`;
    }

    // Display response on UI
    responseBox.innerHTML = `
        <p><b>Query:</b> ${question}</p>
        <p>${displayText}</p>
    `;
}
