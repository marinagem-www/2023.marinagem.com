from os import listdir, path

def get_set_files(dir, ext):
  spath = path.dirname(path.realpath(__file__))
  dext = ".%s" % ext if ext != "" else ""
  return {p.replace(dext, "") for p in listdir(path.join(spath, dir)) if p.endswith(dext)}

projs_en = get_set_files("../projects/en", "md")
projs_pt = get_set_files("../projects/pt", "md")

pages_en = get_set_files("../pages/en", "md")
pages_pt = get_set_files("../pages/pt", "md")

img_dirs = get_set_files("../imgs", "")

if len(projs_en - projs_pt) > 0:
  print("these PT projects are missing: %s" % (projs_en - projs_pt))

if len(projs_pt - projs_en) > 0:
  print("these EN projects are missing: %s" % (projs_pt - projs_en))

if len(projs_pt - img_dirs) > 0:
  print("these PT projects might be missing images: %s" % (projs_pt - img_dirs))

if len(projs_en - img_dirs) > 0:
  print("these EN projects might be missing images: %s" % (projs_en - img_dirs))

if len(pages_en - pages_pt) > 0:
  print("these PT pages are missing: %s" % (pages_en - pages_pt))

if len(pages_pt - pages_en) > 0:
  print("these EN pages are missing: %s" % (pages_pt - pages_en))
