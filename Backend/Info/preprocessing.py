import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer

def preprocess_data(file_path):
    data = pd.read_csv(file_path)

    num_cols = data.select_dtypes(include=['float64', 'int64']).columns
    cat_cols = data.select_dtypes(include=['object']).columns

    num_imputer = SimpleImputer(strategy='mean')
    cat_imputer = SimpleImputer(strategy='most_frequent')

    data[num_cols] = num_imputer.fit_transform(data[num_cols])
    data[cat_cols] = cat_imputer.fit_transform(data[cat_cols])

    encoder = OneHotEncoder(sparse=False, drop='first')
    encoded_cols = pd.DataFrame(encoder.fit_transform(data[cat_cols]), columns=encoder.get_feature_names_out(cat_cols), index=data.index)
    data = pd.concat([data.drop(cat_cols, axis=1), encoded_cols], axis=1)

    scaler = StandardScaler()
    data[num_cols] = scaler.fit_transform(data[num_cols])

    return data
