import csv
import sys
import calendar

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )
    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename):
    if len(sys.argv) != 2:
        print("Usage : python script.py data.csv")
    evidence_list = list()
    label_list = list()
    month_dict = dict( Jan = 0, Feb = 1, Mar = 2, Apr = 3, May = 4, June = 5, Jul = 6, Aug = 7, Sep = 8, Oct = 9, Nov = 10, Dec = 11)

    with open(filename) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            evidence_list.append(
                [int(row["Administrative"]),
                 float(row["Administrative_Duration"]),
                 int(row["Informational"]),
                 float(row["Informational_Duration"]),
                 int(row["ProductRelated"]),
                 float(row["ProductRelated_Duration"]),
                 float(row["BounceRates"]),
                 float(row["ExitRates"]),
                 float(row["PageValues"]),
                 float(row["SpecialDay"]),
                 month_dict[row["Month"]],
                 int(row["OperatingSystems"]),
                 int(row["Browser"]),
                 int(row["Region"]),
                 int(row["TrafficType"]),
                 1 if row["VisitorType"] == "Returning_Visitor" else 0,
                 1 if row["Weekend"] == "TRUE" else 0
                 ]
            )
            label_list.append(1 if row["Revenue"] == "TRUE" else 0)


    loaded_data = (evidence_list, label_list)

    return loaded_data


def train_model(evidence, labels):

    trainModel = KNeighborsClassifier(n_neighbors=1)
    fittedModel = trainModel.fit(evidence,labels)
    return fittedModel

def evaluate(labels, predictions):
    total_true = 0
    total_false = 0
    sensitivity = 0
    specificty = 0

    for i in range(len(labels)):
        if labels[i] == 1:
            total_true += 1
            if predictions[i] == labels[i] :
                sensitivity += 1
        elif labels[i] == 0:
            total_false += 1
            if predictions[i] == labels[i]:
                specificty += 1

    sensitivity = sensitivity/total_true
    specificty = specificty/total_false
    return sensitivity, specificty

if __name__ == "__main__":
    main()
