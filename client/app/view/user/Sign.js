Ext.define('doings.view.user.Sign', {
    extend: 'Ext.panel.Panel',
    alias: 'widget.user_sign',

    title: '用户登录',
    data: [{url:'#', name:'abc'},{url:'#', name:'ert'}],
    tpl: new Ext.XTemplate('<ul><tpl for="."><li><a href="{url}">{name}</a></li></tpl></ul>')
})
