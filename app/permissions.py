from rest_framework import permissions


class GlobalDefaultPermission(permissions.BasePermission):

    # Captura o nome do app
    def get_app_name(self, view) -> str:
        return str(view.queryset.model._meta.app_label)

    # Captura o nome do Model
    def get_model_name(self, view) -> str:
        return str(view.queryset.model._meta.model_name)

    # Captura o nome da ação a ser realizada
    def get_action_name(self, method) -> str:
        methods = {
            'GET': 'view',
            'HEAD': 'view',
            'OPTIONS': 'view',
            'POST': 'add',
            'PUT': 'change',
            'PACTH': 'change',
            'DELETE': 'delete',
        }

        return methods[method]

    # Verifica as permissões do usuário
    def has_permission(self, request, view) -> bool:
        app_name = self.get_app_name(view)
        action_name = self.get_action_name(request.method)
        model_name = self.get_model_name(view)

        if request.user.has_perm(f'{app_name}.{action_name}_{model_name}'):
            return True

        return False
