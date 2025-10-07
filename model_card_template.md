# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
The model that was used was a linear regression model. It was trained on census data to whether income is >50k per year based on census data.

## Training Data
The training data was spit from the main data set. The proportion that was used for training was 80%
## Evaluation Data
The evaluation data was the remaining 20% of the data that was not used for training.
## Metrics
The model was evaluated using accuracy, precision, recall and F1-score. The Precision: 0.7399 | Recall: 0.6047 | F1: 0.6655 with 5000 iterations rans. 
## Ethical Considerations
There could be bias in the data set that could lead to unfair predictions. For example, if the data set has a disproportionate number of individuals from a certain demographic group, the model may learn to make predictions that are biased against that group.
## Caveats and Recommendations

While the model demonstrates reasonable performance based on the evaluation metrics, there are several caveats and recommendations to consider:

1. **Bias in Data**: The model may exhibit biases due to imbalances in the training data. For instance, certain demographic groups (e.g., race, sex, or native-country) may be underrepresented, leading to potential disparities in predictions.

2. **Small Sample Sizes**: Some categories, such as specific native countries, have very small sample sizes (e.g., Cambodia, Hungary). Predictions for these groups may not be reliable and should be interpreted with caution.

3. **Zero Precision or Recall**: Certain groups (e.g., Columbia, Jamaica) have metrics indicating zero precision or recall, which suggests the model struggles to make accurate predictions for these categories.

4. **Generalization**: The model was trained on census data and may not generalize well to other datasets or domains. Users should validate the model on their specific use case before deployment.

5. **Recommendations**:
   - Regularly monitor the model's performance across different demographic groups to ensure fairness and mitigate bias.
   - Consider collecting additional data for underrepresented groups to improve model reliability.
   - Use the model as a decision-support tool rather than relying solely on its predictions, especially in high-stakes scenarios.
