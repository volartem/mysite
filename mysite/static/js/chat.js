var appChat = angular.module('Chat', ['ngWebSocket']);
appChat.config(['$interpolateProvider', function ($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
}]);
appChat.factory('Users', function ($websocket) {
    var users = $websocket('ws://' + window.location.host + '/users/');
    var collection = [];

    users.onOpen(function (val) {
        // console.log('open - user - connect ', val);
    });

    users.onMessage(function (message) {
        var data = JSON.parse(message.data);
        console.log('message.data onMessage users ', message.data);
        console.log('message onMessage users ', message);
        if(data.users){
            collection.push(data);
            console.log('onMessage collection users ', collection);
        }else{
            console.log('message.data onMessage users else ', message.data);
            collection = null;
        }
    });

    users.onClose(function (val) {
        collection = null;
    });

    var methods = {
        collection: collection
    };

    return methods;
});
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

appChat.controller('SomeController', function ($scope, Messages, Users) {
    $scope.message_list = Messages.collection;

    $scope.users = Users.collection;
    // console.log('controller users ', $scope.users);

    $scope.sends = function (val) {
        if (val) {
            Messages.get(val);
        }
    }

});
