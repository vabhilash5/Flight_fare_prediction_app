import datetime


import numpy as np
import pickle
import streamlit as st 

model= pickle.load(open('flight_rf.pkl','rb'))

def welcome():
    return 'Welcome All'

def predict_(row):
    prediction = model.predict([row])
    print(prediction)
    return prediction

def main():
    st.title('Flight Fare Prediction')
    city= ['Banglore', 'Chennai', 'Delhi', 'Kolkata','Mumbai']
    airline= [ 'Air India', 'GoAir', 'IndiGo', 'Jet Airways', 'Jet Airways Business','Multiple carriers','Multiple carriers Premium economy', 'SpiceJet', 'Trujet','Vistara', 
       'Vistara Premium economy']
    Airline = st.selectbox('select Airline',options=airline)
    
    source = st.selectbox('select source place',options=city)
    des_city = ['Banglore','Cochin','Delhi', 'Hyderabad' ,'Kolkata','New Delhi']
    destination = st.selectbox('select destination place',options=des_city)
    total_stops = st.number_input('total stops',step=1)
    dep_date = st.date_input('departure date',datetime.date(2020,5,21))
    dep_time =st.time_input('departure time',datetime.time(5,6,30))
    arr_date = st.date_input('arrival date',datetime.date(2020,5,21))
    arr_time =st.time_input('arrival time',datetime.time(5,6,30))

    pred=0
    if st.button('predict'):
        lst=[0,0,0,0]
        if source!='Banglore':
            lst[city.index(source)-1]=1
        lst1=[0,0,0,0,0]
        if destination!='Banglore':
            lst1[des_city.index(destination)-1]=1
        lst_2=[0,0,0,0,0,0,0,0,0,0,0]
        if Airline!='Air Asia':
            lst_2[airline.index(Airline)]=1
        dep = datetime.datetime.combine(dep_date,dep_time)
        arr = datetime.datetime.combine(arr_date,arr_time)
        dep_hrs = dep.hour
        arr_hrs = arr.hour
        result= (arr-dep).total_seconds()//3600

        inp = [total_stops,dep_hrs,arr_hrs,result]+lst_2+lst+lst1

        pred = model.predict([inp])
    st.success('the output is predicted {}'.format(pred[0]))
if __name__ == '__main__':
    main()