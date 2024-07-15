import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from numerize.numerize import numerize
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
import matplotlib
import warnings

st.set_page_config(
    page_title='Dashboard',
    page_icon='📈',
    layout='wide'
)


st.set_option('deprecation.showPyplotGlobalUse', False)
# Check if the user is authenticated
if not st.session_state.get("authentication_status"):
    st.info('Please log in to access the application from the homepage.')
else:
 
    # Access data from session state
    data = st.session_state.get("data_key", None)
  
    dfz = data.drop(columns=['customerID'])
      
    table_feature = dfz.columns.tolist()
      
    churn_rate = (data["Churn"].sum() / data.shape[0]) * 100
    On_net_calls = data['MonthlyCharges'].sum()
    average_MONTANT_charges = data['TotalCharges'].mean()
    total_revenue = data['TotalCharges'].sum()
    total_Users = data['customerID'].nunique()

    st.markdown("<h5 style='text-align: center;'>KPI's</h5>", unsafe_allow_html=True)
    if data is not None:
        
           with st.container():
                        
                                 #3. columns
                  total1,total2,total3,total4,total5 = st.columns(5,gap='small')
                  with total1:

                     st.markdown('<div class="column-style">Monthly Chrgs</div>', unsafe_allow_html=True)
                     st.metric(label = '', value= f"{On_net_calls:,.0f}")

                     
                     
                  with total2:
                     st.markdown('<div class="column-styl">Avg Income</div>', unsafe_allow_html=True)
                   
                     st.metric(label='', value=f"{average_MONTANT_charges:,.0f}")

                  with total3:
                     st.markdown('<div class="column-sty">Total Charges</div>', unsafe_allow_html=True)
                   
                     st.metric(label= '',value=f"{total_revenue:,.0f}")

                  with total4:
                     st.markdown('<div class="column-st">No_of_Users</div>', unsafe_allow_html=True)
                    
                     st.metric(label='',value=f"{total_Users:,.0f}")

                  with total5:
                     st.markdown('<div class="column-style">Churn Rate %</div>', unsafe_allow_html=True)
                  
                     st.metric(label='',value=numerize(churn_rate),help=f"""Total rating: {churn_rate}""")
      
                  st.markdown("""---""")

                        
                  unsafe_allow_html=True,
               
    def main():
        
         
        st.markdown("<h5 style='text-align: center;'>EDA's</h5>", unsafe_allow_html=True) 

      
        with st.container():
                     
                     data_df= data
                     data_df.columns.tolist()

                     cpp1, cpp2 = st.columns(2)
                     with cpp1:
                        st.title('Univariate Analysis')
                     with cpp2:
                           #selected_uni_feature = st.selectbox('Select Feature', data_df)
                           selected_feature=st.selectbox('Select a Feature', options=table_feature, key='selected_model')

                     co1, co2 = st.columns(2)
                                    
                     with co1:
                           plt.figure(figsize=(8, 6))
                           sns.histplot(data[selected_feature], kde=True)
                           plt.xlabel(selected_feature)
                           plt.title('Histogram')
                           st.pyplot()

                     with co2:
                           plt.figure(figsize=(8, 6))
                           sns.boxplot(data[selected_feature])
                           plt.xlabel(selected_feature)
                           plt.title('Boxplot')
                           st.pyplot()

        with st.container():
                     st.title('Churn rate: For Per Selected Features')           

                     cn1, cn2 = st.columns(2)
                     
                     with cn1:
                           plt.figure(figsize=(8, 6))
                           sns.histplot(data[selected_feature], kde=True)
                           plt.xlabel(selected_feature)
                           plt.title('Histogram')
                           st.pyplot()

                     with cn2:
                           plt.figure(figsize=(8, 6))
                           data[selected_feature].value_counts().plot.pie(autopct='%1.1f%%')
                           plt.ylabel('')
                           plt.title('Pie Chart')
                           st.pyplot()

        with st.container():
                     cppo1, cppo2, cppo3= st.columns(3)
                     with cppo1:
                        st.title('Bivariate  Analysis')
                     with cppo2:
                           #selected_uni_feature = st.selectbox('Select Feature', data_df)
                           selected_feature1=st.selectbox('Select a Feature', options=table_feature, key='selected_modeli')
                     with cppo3:
                           #selected_uni_feature = st.selectbox('Select Feature', data_df)
                           selected_feature2=st.selectbox('Select a Feature', options=table_feature, key='selected_modela')
                     c1, c2 = st.columns(2)
                  
                     with c1:
                           plt.figure(figsize=(8, 6))
                           sns.scatterplot(x=selected_feature1, y=selected_feature2, hue=selected_feature2, data=data)
                           plt.xlabel(selected_feature1)
                           plt.ylabel(selected_feature2)
                           plt.title('Scatter Plot')
                           plt.legend(title=selected_feature2)
                           st.pyplot()

                     with c2:
                           plt.figure(figsize=(8, 6))
                           pivot_data = data.pivot_table(index=selected_feature1, columns=selected_feature2, aggfunc='size')
                           sns.heatmap(pivot_data, cmap='Blues', annot=True, fmt='g')
                           plt.xlabel(selected_feature2)
                           plt.ylabel(selected_feature1)
                           plt.title('Heatmap')
                           st.pyplot()

        with st.container():
                        df1 = data.drop(columns=['customerID','gender'])
                     
                        qppo1, qppo2, qppo3, qppo4, qppo5, qppo6 = st.columns(6)
                        with qppo1:
                           st.header('Multivariate')
                        with qppo2:
                           pass
                        with qppo3:
                           pass   
                        with qppo4:
                           z_variable = st.selectbox("Par1:", df1.columns)  
                        with qppo5:
                           x_variable = st.selectbox("Par2:", df1.columns)
                        with qppo6:
                           y_variable = st.selectbox("Par3:", df1.columns)    
                     
                     
                        ca1, ca2 = st.columns(2)
                        correlation_matrix = df1.corr(numeric_only=True)
                     
                        with ca1:  
                            plt.figure(figsize=(10, 8))
                            sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
                            plt.title("Correlation Matrix")
                            st.pyplot()

                        with ca2:
                            fig = plt.figure(figsize=(10, 8))
                            ax = fig.add_subplot(111, projection='3d')
                            ax.scatter(df1[x_variable], df1[y_variable], df1[z_variable])
                            ax.set_xlabel(x_variable)
                            ax.set_ylabel(y_variable)
                            ax.set_zlabel(z_variable)
                            plt.title("3D Scatter Plot")
                            st.pyplot()

                   
st.markdown(
    """
    <style>
    .column-style {
        background-color: #007bff;
        color: white;
        padding: 20px;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <style>
    .column-styl {
        background-color: #FFA500;
        color: white;
        padding: 20px;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <style>
    .column-sty {
        background-color: #28a745;
        color: white;
        padding: 20px;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <style>
    .column-st {
        background-color: #ff0000;
        color: white;
        padding: 20px;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
          
 
if __name__ == '__main__':
              main()
 
    
 
