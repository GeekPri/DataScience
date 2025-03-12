class Univariate():
    def getQuanQual(dataset):
        qual = []
        quan = []
        for col in dataset.columns:
            if dataset[col].dtype == 'O':
                qual.append(col)
            else:
                quan.append(col)
        return quan, qual
         


