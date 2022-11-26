def imp1(df, **kwargs):
    df_c = df.copy()
    df_c['PAYMENTS'].fillna(df_c['MINIMUM_PAYMENTS'], inplace=True)
    return df_c
    # df['PAYMENTS'].fillna(df['MINIMUM_PAYMENTS'], inplace=True)
    # return df

def imp1_out(self, input_features):
    return self.kw_args['features']