var widgets = require('@jupyter-widgets/base');
var _ = require('lodash');

var FetchModel = widgets.DOMWidgetModel.extend({
  defaults: _.extend(widgets.DOMWidgetModel.prototype.defaults(), {
      _model_name: 'FetchModel',
      _view_name: 'FetchView',
      _model_module: 'ipyfetch',
      _view_module: 'ipyfetch',
      _model_module_version: '0.1.0',
      _view_module_version: '0.1.0',
      result: {},
      value: 'js'
    }
  ),
});


var FetchView = widgets.DOMWidgetView.extend({
  initialize: function () {
    this.model.on('change:url', this.render, this);
  },

  render: function () {
    const request = async () => {
      const response = await fetch(
        this.model.get('url'),
        this.model.get('options')
      );
      const result = await response.json();
      console.log(result);
      this.model.set('value', result);
      this.touch();
    };
    request();
  },


});


module.exports = {
  FetchModel: FetchModel,
  FetchView: FetchView
};
