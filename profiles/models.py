from django.db import models
# Create your models here.


class DnaProfile(models.Model):
    user = models.ForeignKey('users.Profile')

    D8S1179_left = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    D8S1179_right = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    D21S11_left = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    D21S11_right = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    D7S820_left = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    D7S820_right = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    CSF1PO_left = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    CSF1PO_right = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    D3S1358_left = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    D3S1358_right = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    TH01_left = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    TH01_right = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    D13S317_left = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    D13S317_right = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    D16S539_left = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    D16S539_right = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    D2S1338_left = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    D2S1338_right = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    D19S433_left = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    D19S433_right = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    vWA_left = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    vWA_right = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    TPOX_left = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    TPOX_right = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    D18S51_left = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    D18S51_right = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    AMEL_left = models.CharField(max_length=2, null=True)
    AMEL_right = models.CharField(max_length=2, null=True)
    D5S818_left = models.IntegerField(max_length=2, null=True)
    D5S818_right = models.IntegerField(max_length=2, null=True)
    FGA_left = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    FGA_right = models.DecimalField(max_digits=4, decimal_places=1, null=True)

    #objects = DnaProfile()



class DnaProfileManager(models.Manager):
    def search_dna(self, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, aa, bb, cc, dd, ee, ff):
        profile = DnaProfile.objects.filter(D8S1179_left=a, D8S1179_right=b, D21S11_left=c, D21S11_right=d, D7S820_left=e, D7S820_right=f,
                CSF1PO_left=g, CSF1PO_right=h, D3S1358_left=i, D3S1358_right=j, TH01_left=k,TH01_right=l, D13S317_left=m,
                D13S317_right=n, D16S539_left=o, D16S539_right=p, D2S1338_left=q, D2S1338_right=r, D19S433_left=s,
                D19S433_right=t, vWA_left=u, vWA_right=v, TPOX_left=w, TPOX_right=x, D18S51_left=y, D18S51_right=z,
                AMEL_left=aa, AMEL_right=bb, D5S818_left=cc, D5S818_right=dd,
                FGA_left=ee, FGA_right=ff)

        print profile
        return profile



# class DnaProfileManager(models.Manager):
#     def search(self, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, aa, bb, cc, dd,
#                ee, ff):
#         profile = DnaProfile.objects.filter (D8S1179_left=a,
#                                              D8S1179_right=b,
#                                              D21S11_left=c,
#                                              D21S11_right=d,
#                                              D7S820_left=e,
#                                              D7S820_right=f,
#                                              CSF1PO_left=g,
#                                              CSF1PO_right=h,
#                                              D3S1358_left=i,
#                                              D3S1358_right=j,
#                                              TH01_left=k,
#                                              TH01_right=l,
#                                              D13S317_left=m,
#                                              D13S317_right=n,
#                                              D16S539_left=o,
#                                              D16S539_right=p,
#                                              D2S1338_left=q,
#                                              D2S1338_right=r,
#                                              D19S433_left=s,
#                                              D19S433_right=t,
#                                              vWA_left=u,
#                                              vWA_right=v,
#                                              TPOX_left=w,
#                                              TPOX_right=x,
#                                              D18S51_left=y,
#                                              D18S51_right=z,
#                                              AMEL_left=aa,
#                                              AMEL_right=bb,
#                                              D5S818_left=cc,
#                                              D5S818_right=dd,
#                                              FGA_left=ee,
#                                              FGA_right=ff)
#
#         print profile
#         return profile

