from django.contrib import admin
from .models import Post, PostImage, Premium, PremAlbum, Vip, VipAlbum, Category, Contact, FullAlbum, Full, Author, \
    Review
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin


class PostImageAdmin(admin.StackedInline):
    model = PostImage


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    class Meta:
       model = Post


@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass


#-----------------

class PremAlbumAdmin(admin.StackedInline):
    model = PremAlbum


@admin.register(Premium)
class PremAdmin(admin.ModelAdmin):
    inlines = [PremAlbumAdmin]

    class Meta:
       model = Premium


@admin.register(PremAlbum)
class PremAlbumAdmin(admin.ModelAdmin):
    pass


#----------


class VipAlbumAdmin(admin.StackedInline):
    model = VipAlbum


@admin.register(Vip)
class VipAdmin(admin.ModelAdmin):
    inlines = [VipAlbumAdmin]

    class Meta:
       model = Vip


@admin.register(VipAlbum)
class VipAlbumAdmin(admin.ModelAdmin):
    pass


#--------


class FullAlbumAdmin(admin.StackedInline):
    model = FullAlbum


@admin.register(Full)
class FullAdmin(admin.ModelAdmin):
    inlines = [FullAlbumAdmin]

    class Meta:
       model = Full


@admin.register(FullAlbum)
class FullAlbumAdmin(admin.ModelAdmin):
    pass


#-------


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ('name', 'description', 'image')
    pass

# admin.site.register(Category)


@admin.register(Contact)
class ContactAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
    list_display = ('email', 'name', 'text')
    pass


@admin.register(Author)
class AuthorAdmin(ImportExportActionModelAdmin):
    list_display = ('name', 'email')
    pass


@admin.register(Review)
class ReviewAdmin(ImportExportActionModelAdmin):
    list_display = ('title', 'description', 'author')
    pass
