Ext.application({
    name: 'doings',
    appFolder: '/client/app',
    controllers: ['Login'],
    requires: [
        'doings.view.UserLogin'
    ],
    launch : function() {
        Ext.create('doings.view.UserLogin');
    }
});
