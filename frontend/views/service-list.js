var Backbone = require('backbone'),
    template = require("../templates/service-list.hbs"),
    i18n = require('i18next-client'),
    models = require('../models/service')
;

module.exports = Backbone.View.extend({
    initialize: function(){
        this.services = new models.Services();
        this.render();
    },

    render: function() {
        var $el = this.$el;
        var services = this.services;
        this.services.fetch().then(function(r){
            $el.html(template({
                services: services.data(),
            }));
        });
    },

    events: {
    },
})
