import pandas as pd
import datetime

def transformar_columnas(df):
    columns = ['order_purchase_timestamp',
               'order_approved_at', 'order_delivered_carrier_date',
               'order_delivered_customer_date', 'order_estimated_delivery_date']
    for column in columns:
        df[column]=pd.to_datetime(df[column])

def time_dif(df,new_col_name,column_1,column_2):
    df[new_col_name]=df[column_1]- df[column_2]
    return df[new_col_name]

def time_dif_en_dias(df,new_col_name,column_1,column_2):
    df[new_col_name]=df[column_1]- df[column_2]
    one_day_delta = datetime.timedelta(days=1)
    return df[new_col_name]/one_day_delta

def tiempo_de_espera(df,new_col_name,column_1,column_2,is_delivered):
    one_day_delta = datetime.timedelta(days=1)
    if is_delivered:
        #filter=df['order_status'] == "delivered"
        #df= df[filter].copy()
        df.loc[df.order_status == 'delivered',new_col_name]= (df[column_1] - df[column_2])/one_day_delta
        return df
    else:
        df[new_col_name] = (df[column_1] - df[column_2])/ one_day_delta
        return df

