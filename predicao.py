from flask import Flask, render_template, request
import pandas as pd
import pickle


app = Flask(__name__, template_folder='template',
            static_folder='template/assets')


model_rfc = pickle.load(open('C:/Users/gusta/Documents/TADS/ML/loan-classifier/models/pipe.pkl', 'rb'))


@app.route('/')
def home():
    return render_template("homepage.html")


@app.route('/dados_cliente')
def dados_cliente():
    return render_template("form.html")


def get_data():
    Gender = request.form.get('Gender')
    Married = request.form.get('Married')
    Dependents = request.form.get('Dependents')
    Education = request.form.get('Education')
    Self_Employed = request.form.get('Self_Employed')
    ApplicantIncome = request.form.get('ApplicantIncome')
    LoanAmount = request.form.get('LoanAmount')
    

    d_dict = {'Gender': [Gender], 'Married': [Married], 'Dependents': [Dependents],
              'Education': [Education], 'Self_Employed': [Self_Employed], 'ApplicantIncome': [ApplicantIncome],
              'LoanAmount': [LoanAmount]}

    return pd.DataFrame.from_dict(d_dict, orient='columns')


@app.route('/send', methods=['POST'])
def show_data():
    df = get_data()
    # colocar dataframe na ordem das features do modelo
    df = df[['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed',
             'ApplicantIncome', 'LoanAmount']]
    print(df.dtypes)
    df['Dependents'] = df['Dependents'].replace('3+', '3').astype(int)
    df['ApplicantIncome'] = df['ApplicantIncome'].astype(float)
    df['LoanAmount'] = df['LoanAmount'].astype(float)
    df['Married'].unique()  # ['Yes', 'No']
    df['Education'].unique()
    for col in ['Gender', 'Married', 'Education', 'Self_Employed']:
        df[col] = df[col].astype(str)

    print(df.dtypes)
    prediction = model_rfc.predict(df)
    outcome = 'Empréstimo não aprovado. Por favor, revise os critérios ou solicite garantias.'
    imagem = 'chefe_brabo.jpg'
    if prediction == 1:
        outcome = 'Parabéns! Empréstimo aprovado para o cliente.'
        imagem = 'chefe_feliz.jpg'

    return render_template('result.html', tables=[df.to_html(classes='data', header=True, col_space=10)],
                           result=outcome, imagem=imagem)
    # classes: CSS class(es) to apply to the resulting html table


if __name__ == "__main__":
    app.run(debug=True)