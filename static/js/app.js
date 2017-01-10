var app = angular.module('app', ['ngRoute']);
angular.module('app').config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
});
