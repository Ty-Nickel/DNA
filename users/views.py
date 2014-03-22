from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from dna.forms import DnaProfileForm
from profiles.forms import DnaQuickSearch
from users.models import Profile
from profiles.models import DnaProfileManager

# Create your views here.
def users(request):
    user = Profile.objects.all()
    data = {"users": user}
    return render(request, "users.html", data)


def search(request):
    if request.method == 'POST':
        print "post"
        form = DnaQuickSearch(request.POST)
        print form
        if form.is_valid():
            print "is valid"
            a = form.cleaned_data["DBS1179_left"]
            b = form.cleaned_data["DBS1179_right"]
            c = form.cleaned_data["D21S11_left"]
            d = form.cleaned_data["D21S11_right"]
            e = form.cleaned_data["D7S820_left"]
            f = form.cleaned_data["D7S820_right"]
            g = form.cleaned_data["CSF1PO_left"]
            h = form.cleaned_data["CSF1PO_right"]
            i = form.cleaned_data["D3S1358_left"]
            j = form.cleaned_data["D3S1358_right"]
            k = form.cleaned_data["TH01_left"]
            l = form.cleaned_data["TH01_right"]
            m = form.cleaned_data["D13S317_left"]
            n = form.cleaned_data["D13S317_right"]
            o = form.cleaned_data["D16S539_left"]
            p = form.cleaned_data["D16S539_right"]
            q = form.cleaned_data["D2S1338_left"]
            r = form.cleaned_data["D2S1338_right"]
            s = form.cleaned_data["D19S433_left"]
            t = form.cleaned_data["D19S433_right"]
            u = form.cleaned_data["vWA_left"]
            v = form.cleaned_data["vWA_right"]
            w = form.cleaned_data["TPOX_left"]
            x = form.cleaned_data["TPOX_right"]
            y = form.cleaned_data["D18S51_left"]
            z = form.cleaned_data["D18S51_right"]
            aa = form.cleaned_data["AMEL_left"]
            bb = form.cleaned_data["AMEL_right"]
            cc = form.cleaned_data["D5S818_left"]
            dd = form.cleaned_data["D5S818_right"]
            ee = form.cleaned_data["FGA_left"]
            ff = form.cleaned_data["FGA_right"]

            dpm = DnaProfileManager()
            person = dpm.search_dna(a, b, c, d, e, f, g, h, i, j, k, l, m, n,
                                    o, p, q, r, s, t, u, v, w, x, y, z, aa, bb,
                                    cc, dd, ee, ff,)
            if len(person) == 1:
                print person
                data = {"user": person[0].user}
                print person[0].user.first_name
                print person[0].user.last_name
                return render(request, 'users.html', data)
            elif len(person) > 1:
                return HttpResponse("There were more than one matches.")
            else:
                return HttpResponse("Nobody found in our database")
                # return render(request, 'search.html', {'form': form})

        else:
            return HttpResponse("Form is not valid")

        #if form.save():

            #return HttpResponseRedirect('/thanks')
    else:
        form = DnaQuickSearch()
        return render(request, 'search.html', {
            'form': form,
        })

   # def auth(request):
    #    if 'login_button' in request.POST:
     #   return redirect('')
   # else:


def thanks(request):
    return render(request, "thanks.html")

