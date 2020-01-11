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



@app.route('/user/<string:id>', methods=['GET', 'POST'])
def index_id(id):

    print(id)
    table1meta = MetaData(engine)
    table1 = Table('lr_process_history', table1meta, autoload=True)
    DBSession = orm.sessionmaker(bind=engine)
    session = DBSession()
    # results = session.query(table1).order_by(table1.columns.task_create).all()
    search_id = '100000000000'+str(id)
    print(search_id)
    results = session.query(table1).filter(table1.columns.id==int(search_id)).first()

    if results:
        # print(results)
        return render_template('index.html', results=results)
    flash('id {} does not exist'.format(search_id), 'success')
    return redirect(url_for('index'))


@app.route('/transaction/<string:sourceID>')
def index2(sourceID):
    table1meta = MetaData(engine)

    table1 = Table('lr_transaction', table1meta, autoload=True)
    table2 = Table('lr_process_history', table1meta, autoload=True)

    DBSession = orm.sessionmaker(bind=engine)
    session = DBSession()

    transaction = session.query(table1).filter(table1.columns.source_property_ids==sourceID).first()
    process = session.query(table2).filter(table2.columns.transaction_id==transaction.id).first()

    print(process)
    return render_template('index.html', results=process)