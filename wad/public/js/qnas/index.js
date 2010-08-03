/*jslint bitwise: true, eqeqeq: true, forin: true, immed: true, newcap: true, nomen: true, onevar: true, regexp: false, undef: true */

var Ext, WAD, WAD;

WAD.QNA = Ext.extend(Ext.util.Observable, {
        constructor: function (elId, config) {
            config = config || {}
            Ext.apply(this, config);
            WAD.QNA.superclass.constructor.call(this, config);

            this.dt = Ext.get(elId);
            this.dd = this.dt.next();
	    this.a = this.dt.child('a');
	    this.a.dom.removeAttribute('href');
            this.dd.setVisibilityMode(Ext.Element.DISPLAY);
            this.dd.hide();
            this.open = false;

            this.dt.on('click', this.onClick, this);
        },
        onClick: function (ev, el, o) {
            var wasOpen;
            wasOpen = this.open;
            Ext.each(WAD.qnas, function (qna) {
                    if (qna.open) {
                        qna.dd.slideOut();
                        qna.open = false
                    }
                })
            if (!wasOpen) {
                this.dd.slideIn();
                this.open = true;
            }
        }
});

Ext.onReady(function () {
        var dts;
        dts = Ext.query('.qnas dt');
        WAD.qnas = []
        Ext.each(dts, function (dt) {
                WAD.qnas.push(new WAD.QNA(dt));
            });
    });
