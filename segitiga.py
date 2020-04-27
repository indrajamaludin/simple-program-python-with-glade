import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

class hitungSegitiga():
    def segitiga_destroy_cb(self, object, data=None):
        Gtk.main_quit()

    def tmblHitung_clicked_cb(self, object, data=None):
        self.txtAlas = self.builder.get_object("txtAlas")
        self.txtTinggi = self.builder.get_object("txtTinggi")
        self.txtLuas = self.builder.get_object("txtLuas")

        self.alas = float(self.txtAlas.get_text())
        self.tinggi = float(self.txtTinggi.get_text())

        luas = (self.alas*self.tinggi)/2
        self.txtLuas.set_text(str(luas))

    def __init__(self):
        self.gladefile = ("latSegitiga.glade")
        self.builder= Gtk.Builder()
        self.builder.add_from_file(self.gladefile)
        self.builder.connect_signals(self)
        self.window = self.builder.get_object("segitiga")
        self.window.show()
        
if __name__=="__main__":
    main = hitungSegitiga()
    Gtk.main()
