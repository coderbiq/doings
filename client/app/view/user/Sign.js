Ext.define('doings.view.user.Sign', {
    extend: 'Ext.panel.Panel',
    alias: 'widget.user_sign',

    initComponent: function() {
        this.dataview = Ext.create('Ext.view.View', {
            border: false,
            cls: 'review-list',

            autoScroll: true,
            store: 'LoginMethod',
            itemSelector: '.review',
            tpl: new Ext.XTemplate('<ul><tpl for=".">',
                '<li><a href="{url}">{name}</a></li>',
                '</tpl></ul>')
        });

        Ext.apply(this, {
            title: '用户登录',
            layout: 'fit',
            items:[this.dataview]
        });
        this.callParent(arguments);

    }
})
