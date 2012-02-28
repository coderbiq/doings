Ext.application({
    name: 'doings',
    appFolder: '/client/app',
    requires: [
        'doings.view.UserLogin'
    ],
    launch : function() {
        Ext.create('doings.view.UserLogin');
    }
});
