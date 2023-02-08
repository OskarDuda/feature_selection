from diagrams import Diagram
from diagrams.programming.flowchart import StartEnd

with Diagram("REST API endpoints", show=False):
    StartEnd("POST /upload_data")
    StartEnd("POST /score_features")
    StartEnd("GET /feature_importances")
