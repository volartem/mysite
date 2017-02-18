
var app = angular.module('App', ["ngResource"]).config(['$interpolateProvider', function($interpolateProvider){
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
}]).constant("baseUrl", "comments/");

app.config(['$resourceProvider', function($resourceProvider) {
  // Don't strip trailing slashes from calculated URLs
  $resourceProvider.defaults.stripTrailingSlashes = false;
}]);

app.controller("defaultCtrl", function ($scope, $http, $resource, baseUrl) {
    $scope.itemsResource = $resource(baseUrl);
    $scope.refresh = function () {
    // метод query выполняет запрос на сервер и возвращает коллекцию, которая содержит объекты с данными и дополнительными методами
    // которые используются для взаимодействия с данными на сервере $delete, $get, $remove, $save
    $scope.items = $scope.itemsResource.query();
};
    $scope.refresh();
});

app.controller('mainCtrl', ['$scope', '$http', function($scope, $http) {
    console.log('Main ctrl');
    $scope.a = 12;

    var promise = $http.get('comments/', {});
    promise.then(fulfilled, rejected);

    function fulfilled (response) {
        console.log('response', response.data);
        $scope.comments = angular.fromJson(response.data);
    }
    function rejected (error) {
        console.log('response_error', error);
    }
}]);

// angular.element(document).ready(function() {
//     angular.bootstrap(document, ['optionalModuleName'])}
// );
