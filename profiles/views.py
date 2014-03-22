from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from profiles.models import DnaProfile

from users.models import Profile
# Create your views here.


def profiles(request):
    profile = Profile.objects.all()
    data = {"profiles": profile}
    return render(request, "profiles.html", data)


def search(request):
    if request.method == 'POST':
        form = DnaProfile(request.POST)
        if form.is_valid:
            a = form.D8S1179_left
            b = form.D8S1179_right
            c = form.D21S11_left
            d = form.D21S11_right
            e = form.D7S820_left
            f = form.D7S820_right
            g = form.CSF1PO_left
            h = form.CSF1PO_right
            i = form.D3S1358_left
            j = form.D3S1358_right
            k = form.TH01_left
            l = form.TH01_right
            m = form.D13S317_left
            n = form.D13S317_right
            o = form.D16S539_left
            p = form.D16S539_right
            q = form.D2S1338_left
            r = form.D2S1338_right
            s = form.D19S433_left
            t = form.D19S433_right
            u = form.vWA_left
            v = form.vWA_right
            w = form.TPOX_left
            x = form.TPOX_right
            y = form.D18S51_left
            z = form.D18S51_right
            aa = form.AMEL_left
            bb = form.AMEL_right
            cc = form.D5S818_left
            dd = form.D5S818_right
            ee = form.FGA_left
            ff = form.FGA_right


            results = DnaProfile.objects.search(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t,
                                                         u, v, w, x, y, z, aa, bb, cc, dd, ee, ff,)
    else:
        form = DnaProfile()

