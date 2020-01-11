from flask import redirect, request, render_template, flash, url_for
from app import app, db, engine, connection
from sqlalchemy import MetaData, Table, orm, select


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        sourceID = request.form['sourceID']
        try:
            table1meta = MetaData(engine)
            table1 = Table('lr_transaction', table1meta, autoload=True, autoload_with=engine)
            query1 = select([table1]).where(table1.columns.source_property_ids == sourceID)
            result1 = connection.execute(query1).fetchone()

        except Exception as e:
            flash('Encountered an error ({}). Ensure that there is internet connection'.format(e), 'danger')
            return redirect(url_for('index'))

        if result1:
            return redirect(url_for('transaction', sourceID=sourceID))
        flash('ID not found', 'danger')
        return redirect(url_for('index'))

    return render_template('index.html')


@app.route('/trans/<string:sourceID>')
def transaction(sourceID):

    table1meta = MetaData(engine)
    table1 = Table('lr_transaction', table1meta, autoload=True, autoload_with=engine)
    table2 = Table('lr_process_history', table1meta, autoload=True, autoload_with=engine)

    query1 = select([table1]).where(table1.columns.source_property_ids==sourceID)
    result1 = connection.execute(query1).fetchone()
    # print(result1)

    query2 = select([table2]).where(table2.columns.transaction_id==result1.id)
    result2 = connection.execute(query2).fetchone()
    print(result2)

    return render_template('table.html', result=result2, id=sourceID)


