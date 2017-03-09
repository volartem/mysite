var app = angular.module('App', ["ngResource"]);
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
        $scope.items = $scope.itemsResource.query();
    };
    $scope.refresh();

    $scope.create = function (item, parent) {
        item.parent = parent;
        new $scope.itemsResource(item).$save().then(function (newItem) {
            $scope.refresh();
        });
    }
});
