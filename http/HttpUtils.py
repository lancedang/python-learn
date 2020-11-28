import os
import sys
import requests
import json


class HttpUtil:

    def get(url, request):
        return requests.get(url, request)

    def post(url, request):
        return requests.post(url, request)

class StudentService:
    def getStudentById(url, param):
        response = HttpUtil.get(url, param)
        responseJson = response.content
        responseObject = json.loads(responseJson)
        return responseObject['data']


    def updateStudent(url, student):
        response = HttpUtil.post(url, student)
        responseJson = response.content;
        responseObject = json.loads(responseJson)
        return responseObject['data']


if __name__ == "__main__":
    path = "/test/"
    url = "http://localhost:8080" + path

    """get"""
    param = {'id': sys.argv[1]}
    student = StudentService.getStudentById(url, param )
    print(student)

    """update"""
    request = {"name": "lisi", "age": 10}
    newStudent = StudentService.updateStudent(url, request)
    print(newStudent)
    print(newStudent['age'])
