import win32com.client, MSO, MSPPT

g = globals()
for c in dir(MSO.constants): g[c] = getattr(MSO.constants, c)
for c in dir(MSPPT.constants): g[c] = getattr(MSPPT.constants, c)

Application = win32com.client.Dispatch("PowerPoint.Application")
Application.Visible = False
Presentation = Application.Presentations.Add()
Slide = Presentation.Slides.Add(1, ppLayoutBlank)

