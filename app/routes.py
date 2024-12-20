
from flask import Blueprint, render_template, request
from .model import predict_cancer
from .forms import InputForm

bp = Blueprint('main', __name__)

@bp.route('/', methods=['GET', 'POST'])
def home():
    form = InputForm()
    if form.validate_on_submit():
        try:
        # Extract features from the form input
            features = [
            float(form.radius.data),
            float(form.texture.data),
            float(form.perimeter.data),
            float(form.area.data),
            float(form.smoothness.data),
            float(form.compactness.data),
            float(form.concavity.data),
            float(form.concave_points.data),
            float(form.symmetry.data),
            float(form.fractal_dimension.data)
            ]
        
            # Get the prediction
            prediction = predict_cancer(features)

            # Render result page with the prediction
            return render_template('result.html', prediction=prediction)
        except Exception as e:
            return render_template('home.html', form=form, error=str(e))
    return render_template('home.html', form=form)