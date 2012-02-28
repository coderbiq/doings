Ext.define('doings.store.LoginMethod', {
    extend: 'Ext.data.Store',
    fields: ['url', 'name'],
    data: [
        {url:'#', name:'新浪微博登录'}
    ],
});
