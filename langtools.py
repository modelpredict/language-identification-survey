import pycountry


def get_iso_alpha3(label):
    if not label:
        return None

    if label == 'zh-cn':
      return 'cmn'

    if len(label) == 2:
        lang = pycountry.languages.get(alpha_2=label)
    else:
        lang = pycountry.languages.get(alpha_3=label)
    if lang:
        return lang.alpha_3
    return label

