var app = angular.module('App', ["ngResource", "ngSanitize"]);
app.config(['$interpolateProvider', function ($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
}]);
app.config(['$resourceProvider', function ($resourceProvider) {
    $resourceProvider.defaults.stripTrailingSlashes = false;
}]);
app.config(['$httpProvider', function ($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);
app.constant("baseUrl", "comments/");
app.filter('capitalize', function () {  // filter capitalize for templates
    return function (input) {
        return (!!input) ? input.charAt(0).toUpperCase() + input.substr(1).toLowerCase() : '';
    }
});


app.controller("defaultCtrl", function ($scope, $http, $resource, baseUrl) {
    $scope.itemsResource = $resource(baseUrl);

    $scope.refresh = function () {
        // метод query выполняет запрос на сервер и возвращает список комментариев
        $scope.items = $scope.itemsResource.query();
    };
    $scope.refresh();

    // создание нового коммента
    $scope.create = function (item) {
        new $scope.itemsResource(item).$save().then(function (newItem) {
            $scope.items.push(newItem);
        });
    }
});
app.controller("mainCtrl", ['$scope', '$http', '$resource', 'baseUrl', function ($scope, $http, $resource, baseUrl) {
    $scope.itemsResource = $resource('note/' + ":id", {id: "@id"});

    $scope.refresh = function () {
        // метод query выполняет запрос на сервер и возвращает список комментариев
        $scope.notes = $scope.itemsResource.query();
    };
    $scope.refresh();

    $scope.testClick = function (item) {
        // console.log("testClick");
        item.$get().then(function (response) {
            // console.log(response);
            $scope.notes = [];
            $scope.notes[0] = response;
        });
    };
}]);
