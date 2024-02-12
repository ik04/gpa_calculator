from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import CalculateSerializer
from rest_framework import status




@api_view(["POST"])
def calculate(request):
    grade_points =  {
    "O":10,
    "A+":9,
    "A":8,
    "B+":7,
    "B":6,
    "C":5.5,
    "W":0,
    "F":0,
    "Ab":0,
    "I":0,
    "*":0
    }

    data = request.data
    print(data)
    serializer = CalculateSerializer(data=data)
    if not serializer.is_valid:
        return Response({"errors":serializer.errors},status=status.HTTP_400_BAD_REQUEST)

    points = 0
    sum_credits = 0
    
    for entry in data["entries"]:
        print(entry)
        credit = entry['credit']
        grade = entry['grade']
        
        if credit == "":
            credit = 0
        else:
            credit = int(credit)
        
        sum_credits += credit
        gradept = grade_points[grade]
        points += credit * gradept
    
    gpa = points / sum_credits
    percent = int(gpa * 10)
    return Response({"gpa":gpa,"percentage":percent},status=status.HTTP_200_OK)
