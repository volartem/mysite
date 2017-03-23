var appChat = angular.module('Chat', ['ngWebSocket']);
appChat.config(['$interpolateProvider', function ($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
}]);
appChat.factory('Messages', function ($websocket) {
    var dataStream = $websocket('ws://' + window.location.host + '/chat/');
    var collection = [];

    dataStream.onMessage(function (message) {
        if (collection.length == 0) {
            collection.push(JSON.parse(message.data).messages);
        } else {
            collection[0].push(JSON.parse(message.data));
        }

    });

    var methods = {
        collection: collection,

        get: function (val) {
            dataStream.send(val);
        }
    };

    return methods;
});

appChat.controller('SomeController', function ($scope, Messages) {
    var dataStream = new WebSocket('ws://' + window.location.host + '/users/');

    dataStream.onmessage = function (event) {
        $scope.users = JSON.parse(event.data).users;
        $scope.$apply();
    };

    $scope.message_list = Messages.collection;

    $scope.sends = function (val) {
        if (val) {
            Messages.get(val);
        }
    }

});
