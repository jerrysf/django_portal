from django.http import HttpResponse
from django.template import RequestContext, loader

from polls.models import Products, TDD_LTE_Phases, WMP_Phases, DCM_Phases


def index_validator(table):
    try:
        name = table.objects.order_by('-product_id')[0]
    except IndexError:
        name = 'null'
    return name

def index(request):
    #Get latest data from each Product/Subcomponent
    latest_tdlte = TDD_LTE_Phases.objects.order_by('-product_id')[0]
    latest_wmp = WMP_Phases.objects.order_by('-product_id')[0]
    latest_dcm = index_validator(DCM_Phases)
    template = loader.get_template('polls/index.html')
    #Add latest data into context, and pass it to overview page.
    context = RequestContext(request, {
        'latest_tdlte': latest_tdlte,
        'latest_wmp':latest_wmp,
        'latest_dcm':latest_dcm,
    })
    return HttpResponse(template.render(context))
    
def detail(request, product_id):
    return HttpResponse("You're looking at Products %s." % product_id)

def results(request, products_id):
    response = "You're looking at the results of Products %s."
    return HttpResponse(response % products_id)

def vote(request, products_id):
    return HttpResponse("You're voting on Products %s." % products_id)
    
# Chart generation    
from chartit import DataPool, Chart

def chart_view_with_parameter(request, chart_name):
    
    template = loader.get_template('polls/chart.html')

    #Step 1: Create a DataPool with the data we want to retrieve.
    tdlte = \
        DataPool(
           series=
            [{'options': {
               'source': eval(chart_name).objects.all()},
              'terms': [
                'id',
                'entity_build',
                'majorRegression',
                'neve']}
             ])            
             
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = tdlte,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'id': [
                    'entity_build',
                    'majorRegression',
                    'neve']
                  }}],
            chart_options =
              {'title': {
                   'text': 'Entity build history for ' + chart_name},
               'xAxis': {
                    'title': {
                       'text': 'Product ID'}}})
                       
                       
    #Step 3: Send the chart object to the template.
    context = RequestContext(request, {
        'charts': cht,
    })
    
    return HttpResponse(template.render(context))

    
def chart_view(request):
    
    template = loader.get_template('polls/chart_selector.html')

    #Step 1: Create a DataPool with the data we want to retrieve.
    tdlte = \
        DataPool(
           series=
            [{'options': {
               'source': WMP_Phases.objects.all()},
              'terms': [
                'id',
                'entity_build',
                'majorRegression',
                'neve']}
             ])            
             
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = tdlte,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'id': [
                    'entity_build',
                    'majorRegression',
                    'neve']
                  }}],
            chart_options =
              {'title': {
                   'text': 'Entity build history for WMP_Phases'},
               'xAxis': {
                    'title': {
                       'text': 'Product ID'}}})
                       
                       
    #Step 3: Send the chart object to the template.
    context = RequestContext(request, {
        'charts': cht,
    })
    
    return HttpResponse(template.render(context))
    