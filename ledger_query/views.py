from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import re

from utils import ledger_api


@csrf_exempt
@login_required
def transactions(request):
    with open(request.user.ledgerpath.path, 'r') as ledger_fd:
        entries = list(ledger_api.read_entries(ledger_fd))

    transaction_regexp = request.GET.get('regexp')
    if transaction_regexp:
        entries = [
            entry for entry in entries
            if re.fullmatch(transaction_regexp, entry['payee'])
        ]

    return JsonResponse({'entries': entries})