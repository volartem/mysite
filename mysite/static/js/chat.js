var appChat = angular.module('Chat', ['ngWebSocket']);
appChat.config(['$interpolateProvider', function ($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
}]);
appChat.factory('Messages', function ($websocket) {
    var dataStream = $websocket('wss://' + window.location.host + '/ws/chat/');
    var collection = [];

    dataStream.onMessage(function (message) {
        if (collection.length == 0) {
            let response = JSON.parse(message.data);
            collection.push(response.messages);
        } else {
            collection[0].push(JSON.parse(message.data).messages);
        }
    });

    var methods = {
        collection: collection,

        get: function (val) {
            dataStream.send(JSON.stringify({message: val}));
        }
    };

    return methods;
});

appChat.controller('SomeController', function ($scope, Messages) {
    var dataStream = new WebSocket('wss://' + window.location.host + '/ws/users/');

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
