'''
Bank Transfer System
'''

__author__ = 'Dilmuratjohn'

import sys
import pymysql

class Transfer(object):

    def __init__(self,connection):
        self.connection = connection

    def check_account(self,account):
        print("checking account[%s]..." %(account))
        cursor=self.connection.cursor()
        try:
            sql = "select * from account where accountID=%s" %(account)
            cursor.execute(sql)
            rows = cursor.fetchall()
            if len(rows)!=1:
                raise Exception("Account %s does not exist" %(account))
        finally:
            cursor.close()
            print("account checked")

    def check_balance(self,account,transfer_amount):
        print("checking balance ...")
        cursor=self.connection.cursor()
        try:
            sql = "select * from account where accountID=%s and balance>%s" %(account,transfer_amount)
            cursor.execute(sql)
            rows = cursor.fetchall()
            if len(rows)!=1:
                raise Exception("Account %s's balance is insufficient" %(account))
        finally:
            cursor.close()
            print("balance checked")

    def withdrawals(self,account,balance):
        print("making withdrawals...")
        cursor=self.connection.cursor()
        try:
            sql = "update account set balance = balance-%s where accountID=%s " %(transfer_amount,account)
            cursor.execute(sql)
            rows = cursor.fetchall()
            if cursor.rowcount !=1:
                raise Exception("withdrawals failure" %(account))
        finally:
            cursor.close()
            print("withdrawals accomplished")

    def deposit(self,account,balance):
        print("making deposit...")
        cursor=self.connection.cursor()
        try:
            sql = "update account set balance = balance+%s where accountID=%s " %(transfer_amount,account)
            cursor.execute(sql)
            rows = cursor.fetchall()
            if cursor.rowcount !=1:
                raise Exception("deposit failure" %(account))
        finally:
            cursor.close()
            print("deposit accomplished")

    def transfer(self,source_account,transfer_account,transfer_amount):
        try:
            self.check_account(source_account)
            self.check_account(transfer_account)
            self.check_balance(source_account,transfer_amount)
            self.withdrawals(source_account,transfer_amount)
            self.deposit(transfer_account,transfer_amount)
            self.connection.commit()
        except Exception as e:
            self.connection.rollback()
            raise e

if __name__=="__main__":
    source_account = account1
    transfer_account = account2
    transfer_amount = aomunt_of_money

    connection = pymysql.connect(
                                 host='***.***.***.***',
                                 port=PORT,
                                 user='username',
                                 password='******',
                                 db='database',
                                 charset='utf8')

    Transfer_=Transfer(connection)

    try:
        Transfer_.transfer(source_account,transfer_account,transfer_amount)
    except Exception as e:
        print("Error:"+str(e))
    finally:
        connection.close()
