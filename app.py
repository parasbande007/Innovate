from flask import jsonify, render_template

@app.route("/tickets")
def get_tickets():
    all_tickets = list(tickets.find({}, {'_id': 0}))  # Exclude Mongo _id
    return jsonify(all_tickets)

@app.route("/mytickets")
def tickets_page():
    return render_template("tickets.html")


# mongodb+srv://paras23:@KEQN9.s!@Yrr!7@cluster0.gblidbt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0