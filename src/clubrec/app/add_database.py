from pymysql import Date, cursors, connect
from app import db

def companySponsorship (companyId:int, cludId:int, startDate:Date, endDate:Date) -> int:
    db.raw_connection().cursor()
    cursor = db.raw_connection().cursor()
    noOffers = 0
    args = (companyId, cludId, startDate, endDate, noOffers)
    result_args = cursor.callproc('company_sponsorship', args)
    cursor.execute('select @total_offers')  # no other way to get it :-( considerable time to find this, may be different library than pymysql?
    row = cursor.fetchall()
    for item in row:
        noOffers = int(item[0])
    cursor.close()
    return noOffers