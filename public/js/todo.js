var todoApp = angular.module('todoApp', []);

todoApp.controller('TodoController', function($scope, $http) {

  $scope.todos = [];

  $scope.addTodo = function(title) {
    $scope.newTodoTitle = '';
    $scope.todos.push({
        title: title,
        completed: false,
        id: generateID()
    });
  };

  $scope.changeCompleted = function(todo) {
    // Update the todo
    var message = (todo.completed === true) ? 'Task Completed!' : 'Task Uncompleted!';
  };

  $scope.removeCompletedItems = function() {
    $scope.todos.forEach(function(todo) {
        if (todo.completed === true) {
            deleteTodo(todo.id);
        }
    });
  };

  function deleteTodo(id) {
      $scope.todos.forEach(function(todo, i) {
          if (todo.id === id) {
              return $scope.todos.splice(i, 1);
          }
      });
  }
  
  function generateID() {
      var rand = Math.random();
      $scope.todos.forEach(function(todo) {
          if (todo.id === rand) {
             generateID(); 
          }
      });
      return rand;
  }

});