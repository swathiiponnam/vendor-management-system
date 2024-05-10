from django.shortcuts import render
from .models import *
from app.serializers import vendorser,po_ser,his_per_ser
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import parsers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])
def vendors(request):
    if request.method == 'GET':
        records = vendor.objects.all()
        ser=vendorser(records,many=True)
        return Response(ser.data)
    
    elif request.method=='POST':
        da=vendorser(data=request.data)
        if da.is_valid():
            da.save()
            return Response(da.data,status=status.HTTP_201_CREATED)
        else:
            return Response(da.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def vendor_detail(request, pk):
    try: 
        var = vendor.objects.get(pk=pk) 
    except vendor.DoesNotExist: 
        return JsonResponse({'message': 'The vendor does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        var_serializer = vendorser(var) 
        return JsonResponse(var_serializer.data) 
 
    elif request.method == 'PUT': 
        var_serializer = vendorser(var, data=request.data) 
        if var_serializer.is_valid(): 
            var_serializer.save() 
            return JsonResponse(var_serializer.data) 
        return JsonResponse(var_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        var.delete() 
        return JsonResponse({'message': 'vendor data was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

    


@api_view(['GET','POST'])
def po(request):
    if request.method == 'GET':
        records = purchase_order.objects.all()
        ser=po_ser(records,many=True)
        return Response(ser.data)
    
    elif request.method=='POST':
        da=po_ser(data=request.data)
        if da.is_valid():
            da.save()
            return Response(da.data,status=status.HTTP_201_CREATED)
        else:
            return Response(da.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def po_detail(request, pk):
    try: 
        po = purchase_order.objects.get(pk=pk) 
    except purchase_order.DoesNotExist: 
        return JsonResponse({'message': 'The purchase order does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        po_serializer = po_ser(po) 
        return JsonResponse(po_serializer.data) 
 
    elif request.method == 'PUT': 
        po_serializer = po_ser(po, data=request.data) 
        if po_serializer.is_valid(): 
            po_serializer.save() 
            return JsonResponse(po_serializer.data) 
        return JsonResponse(po_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        po.delete() 
        return JsonResponse({'message': 'purchase order was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def ven_per_id(request,pk):
    try:
        history = historical_performance.objects.get(pk=pk)
    except historical_performance.DoesNotExist:
        return JsonResponse({'message' : 'the performance evalution does not exist'},status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        his_ser = his_per_ser(history)
        return JsonResponse(his_ser.data)
    
    

