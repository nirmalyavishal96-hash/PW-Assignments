import http from 'k6/http';
import { check } from 'k6';

export default function () {

    let res = http.get('http://127.0.0.1:5000/hello');

    check(res, {
        'status was 200': (r) => r.status == 200,
    });
}
