Ext.define('doings.view.UserLogin', {
    extend: 'Ext.Viewport',
    requires: [
        'doings.view.user.Sign'
    ],

    layout: 'anchor',
    items: [
        {
            id:'sign',
            xtype: 'user_sign',
            width: 300,
            height: 200,
        }
    ]
});
