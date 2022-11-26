def imp1(df, **kwargs):
    df['PAYMENTS'].fillna(df['MINIMUM_PAYMENTS'], inplace=True)
    return df

def imp1_out(self, input_features):
    return self.kw_args['features']