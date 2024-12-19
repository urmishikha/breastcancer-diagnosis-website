# app/forms.py
from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import InputRequired

class InputForm(FlaskForm):
    radius = FloatField('Mean Radius', validators=[InputRequired()])
    texture = FloatField('Mean Texture', validators=[InputRequired()])
    perimeter = FloatField('Mean Perimeter', validators=[InputRequired()])
    area = FloatField('Mean Area', validators=[InputRequired()])
    smoothness = FloatField('Mean Smoothness', validators=[InputRequired()])
    compactness = FloatField('Mean Compactness', validators=[InputRequired()])
    concavity = FloatField('Mean Concavity', validators=[InputRequired()])
    concave_points = FloatField('Mean Concave Points', validators=[InputRequired()])
    symmetry = FloatField('Mean Symmetry', validators=[InputRequired()])
    fractal_dimension = FloatField('Mean Fractal Dimension', validators=[InputRequired()])
    submit = SubmitField('Diagnose')
