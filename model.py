from pyfasttext import FastText
model = FastText('category_model.bin')

def predict(comment):
    #return 1
    return model.predict_proba_single('%s\n' % comment, k=2)