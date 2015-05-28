import sublime,sublime_plugin,string

class ReplacerCommand(sublime_plugin.TextCommand):
	def run(self,edit):
		for r in reversed(self.view.sel()):
			for line in reversed(self.view.lines(r)):
				text = self.view.substr(line)
				text = text.replace('á', '&aacute;')
				text = text.replace('Á', '&Aacute;')
				text = text.replace('ã', '&atilde;')
				text = text.replace('Ã', '&Atilde;')
				text = text.replace('â', '&acirc;')
				text = text.replace('Â', '&Acirc;')
				text = text.replace('à', '&agrave;')
				text = text.replace('À', '&Agrave;')
				text = text.replace('é', '&eacute;')
				text = text.replace('É', '&Eacute;')
				text = text.replace('ê', '&ecirc;')
				text = text.replace('Ê', '&Ecirc;')
				text = text.replace('í', '&iacute;')
				text = text.replace('Í', '&Iacute;')
				text = text.replace('ó', '&oacute;')
				text = text.replace('Ó', '&Oacute;')
				text = text.replace('õ', '&otilde;')
				text = text.replace('Õ', '&Otilde;')
				text = text.replace('ô', '&ocirc;')
				text = text.replace('Ô', '&Ocirc;')
				text = text.replace('ú', '&uacute;')
				text = text.replace('Ú', '&Uacute;')
				text = text.replace('ç', '&ccedil;')
				text = text.replace('Ç', '&Ccedil;')
				self.view.replace(edit, line, text)
		self.view.erase_status('replacer')
		sublime.status_message('Replaced :)')